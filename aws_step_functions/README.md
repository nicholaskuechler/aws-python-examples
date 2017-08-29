# aws-python-examples
AWS Examples in Python

## AWS Step Functions Python Example

### Prequisites

1. Create a new activity in AWS Step Functions
   1. In the AWS console, browse to Step Functions then Tasks
   2. On the tasks page, click 'Create new activity' button
   3. Give your new activity a name, such as 'example1'
   4. Copy your new activity ARN as we will use this later.

2. Create a new state machine in AWS Step Functions
    1. In the AWS console, browse to Step Functions dashboard
    2. Click 'Create a state machine' button
    3. Give your new state machine a name, such as 'example1'
    4. Select the 'Custom' blueprint
    5. Use this code for your state machine, setting the 'Resource' to the ARN created in step 1.

        ```
        {
          "Comment": "An example using a Task state.",
          "StartAt": "getGreeting",
          "Version": "1.0",
          "TimeoutSeconds": 300,
          "States":
          {
            "getGreeting": {
              "Type": "Task",
              "Resource": "INPUT_THE_ARN_OF_YOUR_ACTIVITY_FROM_STEP_1",
              "End": true
            }
          }
        }
        ```

    6. Copy your new state machine ARN as we will use this later.

3. Edit the example aws_step_functions_python_demo_1.py and set the ARN of your activity from step 1, and the ARN of your state machine from step 2.

    ```
    ACTIVITY_ARN = "arn:aws:states:xxxxxxxxx:123456789012:activity:example1"
    STATE_MACHINE_ARN = "arn:aws:states:xxxxxxxxx:123456789012:stateMachine:example1"
    ```

4. Run the aws_step_functions_python_demo_1.py code:

    ```
    python aws_step_functions_python_demo_1.py
    ```

5. In AWS console for Step Functions, click on dashboard, then click on your example state machine.
    1. Click 'New execution' button
    2. Use the default JSON:

        ```
        {
            "Comment": "Insert your JSON here"
        }
        ```

    3. Click the 'Start Execution' button

5. Go back to your running aws_step_functions_python_demo_1.py and you will see output showing the activity has been executed.

6. In the AWS console, you can drill down to your example state machine's executions and see the completed execution, including input and output JSON.
