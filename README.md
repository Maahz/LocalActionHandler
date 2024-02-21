# Streamer.bot Local Action Handler

This Python application serves as a local interface for executing actions within Streamer.bot via its HTTP Server. By leveraging the DoAction API endpoint, the app enables streamlined action execution directly from the command line, facilitating automation and integration with other software tools.
##Features

- **Simple Command Line Interface: Execute Streamer.bot actions by simply specifying the action name as a command line argument.
- **Flexible Configuration: Pre-configured to connect to the local Streamer.bot HTTP Server with default settings, but allows for easy adjustments if your setup differs.
- **Action Arguments Support: Though not required for basic usage, the app is designed to accommodate additional arguments for actions, providing versatility for complex commands.

## Usage

To execute an action, run the application with the desired action name as a parameter. Here's the syntax for running an action:

## Example

To execute an action named "MyAction":

```Powershell
python action_handler.py MyAction
```

This command sends a POST request to the Streamer.bot's DoAction API endpoint, triggering the specified action.
## Technical Details

The application constructs a POST request containing the action name (and optionally, additional arguments) in JSON format. It then sends this request to the Streamer.bot HTTP Server's DoAction endpoint. A successful request will result in the specified action being executed by Streamer.bot.
## Configuration

By default, the application is configured to connect to the Streamer.bot HTTP Server running locally on port 7474. These settings can be adjusted within the script to match your specific Streamer.bot setup.
## Response Handling

After sending the POST request, the application checks the HTTP response status code. A status code of 204 indicates that the action was successfully executed. If any other status code is received, the application will report a failure along with the response details for troubleshooting.
## Conclusion

This Streamer.bot Local Action Handler offers a convenient way to automate and integrate action execution within Streamer.bot, enhancing the capabilities of your streaming setup with the power of automation.
