# Metal templates configuration

If you want to configure custom metal templates, you should:

1. Setup `cloudrock.metalTemplating.metalTemplatesPath`
    in values.yaml (by default, it is equal to `metal_templates`)

1. Put all the custom template files in the mentioned directory
    with respect to their placement in the source code repository.
    For example, if you want to replace default `cloudrock_core/users/templates/users/invitation_approved_message.html`,
    you should put custom `invitation_approved_message.html`
    file into `<metalTemplatesPath>/cloudrock_core/users/templates/users/` directory.
    Hence, the custom template will present in
    `<metalTemplatesPath>/cloudrock_core/users/templates/users/invitation_approved_message.html`
    file.
