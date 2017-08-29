#!/usr/bin/env python
# Author: Nicholas Kuechler
# URL: http://nicholaskuechler.com
# GitHub: https://github.com/nicholaskuechler

import boto3
import json
import pprint

ACTIVITY_ARN = "arn:aws:states:xxxxxxxxx:123456789012:activity:example1"
STATE_MACHINE_ARN = "arn:aws:states:xxxxxxxxx:123456789012:stateMachine:example1"  # noqa

sfn = boto3.client('stepfunctions')

pp = pprint.PrettyPrinter(indent=4)

# List all the available state machines. The response is in JSON.
print("Listing state machines:")
response = sfn.list_state_machines()
pp.pprint(response)
print("")

# List all the available state machines. The response is in JSON.
print("Listing activities:")
response = sfn.list_activities()
pp.pprint(response)
print("")

# List all the available state machines. The response is in JSON.
print("Listing executions:")
response = sfn.list_executions(stateMachineArn=STATE_MACHINE_ARN)
pp.pprint(response)
print("")

print("")

# Run a custom step functions worker
print("Starting the custom worker example")
response = sfn.get_activity_task(
    activityArn=ACTIVITY_ARN,
    workerName='worker_example_1'
)
pp.pprint(response)
print("")

# Collect the input data and task token
demo_input_raw = response.get('input', {})
demo_input = json.loads(demo_input_raw)
demo_task_token = response.get('taskToken')

print("Got input: %s" % (demo_input))
print("")

# Send a heartbeat to let step functions know we're still working on the task.
response = sfn.send_task_heartbeat(
    taskToken=demo_task_token
)
pp.pprint(response)
print("")

# We can simulate a step function failure by setting success_status to False
success_status = True

if success_status:
    success_output = {'status': 'success'}
    # Emit a success notification back to the state machine, along with the
    # output from our task
    response = sfn.send_task_success(
        taskToken=demo_task_token,
        output=json.dumps(success_output)
    )
    pp.pprint(response)
    print("")
else:
    # Emit a failure noitification back to the state machine, along with an
    # error message and the reason for failure.
    response = sfn.send_task_failure(
        taskToken=demo_task_token,
        error=("An arbitrary error code that identifies the cause of the "
               "failure."),
        cause=("A more detailed explanation of the cause of the failure.")
    )
    pp.pprint(response)
    print("")

# All done. You can check the execution history for your state machine to see
# the response.
print("Finished running worker")
