# Cloudrock Marketplace script plugin setup

Available options in `values.yaml`:

- `cloudrock.marketplace.script.enabled` - enable/disable plugin
- `cloudrock.marketplace.script.dockerImages` - key-value structure, where key is a programming language
  and value - a corresponding docker image tag
- `cloudrock.marketplace.script.k8sNamespace` - Kubernetes namespace, where jobs will be executed
- `cloudrock.marketplace.script.kubeconfigPath` - path to local file with kubeconfig content
- `cloudrock.marketplace.script.jobTimeout` - timeout for Kubernetes jobs
