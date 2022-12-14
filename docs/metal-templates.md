# Metal templates configuration

If you want to configure custom metal templates, you should:

1. Setup `cloudrock.metalTemplating.metalTemplatesPath`
    in values.yaml (by default, it is equal to `metal_templates/metal-templates.yaml`)

2. Put all the custom templates into the file in a following way:

**NB**: The keys in the file should have `<cloudrock_application_name>/<event_name>_<postfix>.<extension>`, where `<postfix>` can be either `message` or `subject`, and `<extension>` - either `txt` or `html`

```yaml
<file-name1>: |
    <Custom content1>
<file-name2>: |
    <Custom content2>
...
```
Example:
```yaml
users/invitation_notification_message.txt: |
    Hi!
users/invitation_notification_message.html: |
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Invitation has been created</title>
    </head>
    <body>
    <p>
        Hi!
    </p>
    </body>
    </html>
...
```
