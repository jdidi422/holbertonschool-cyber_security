# Catch The Flag #1 – Host Header Injection

In this task, the objective was to exploit a Host Header Injection vulnerability in order to poison a password reset link.

The expected attack flow was the following:
- Identify an endpoint that triggers a password reset process
- Inject a malicious Host header pointing to a controlled server
- Start a local HTTP server to capture the reset token
- Wait for the automated bot to click the reset link
- Use the token to reset the password and retrieve the flag from the header

I correctly set up the listening server and crafted requests with injected Host and X-Forwarded-Host headers.

However, in the current lab environment, the routes referenced in the exercise documentation (such as /ticket and /support) are not exposed and consistently return 404 responses. Because of this, the password reset workflow is never triggered and the automated bot does not send any request to the listening server.

As a result, the flag cannot be generated in the current deployment, even though the exploitation logic and methodology were correctly followed.

