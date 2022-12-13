# Migration from Postgresql HA

Plan:

1. Scale api, beat, worker -> 0
1. Backup — using backup job
1. group_vars/puhuri_core_prd - helm_pg_ha_enabled: no ===> CANCEL THE UPDATING PIPELINE!
1. Run dependency update ==> leads to a working single psql
1. Restore DB — using recovery job
1. Run a common update pipeline
1. Validate that login works
1. Drop old psql ha, drop pvc

```bash
# Backup
kubectl exec -it postgresql-ha-cloudrock-postgresql-0 -- env PGPASSWORD=cloudrock pg_dump -h 0.0.0.0 -U cloudrock cloudrock | gzip -9 > backup.sql.gz

# Backup restoration
# Locally
kubectl cp backup.sql.gz postgresql-cloudrock-0:/tmp/backup.sql.gz
kubectl exec -it postgresql-cloudrock-0 -- bash

# In pgpool pod
gzip -d /tmp/backup.sql.gz
export PGPASSWORD=cloudrock
psql -U cloudrock -h 0.0.0.0 -f /tmp/backup.sql
```
