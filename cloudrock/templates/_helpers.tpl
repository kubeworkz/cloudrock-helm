{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "cloudrock.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "cloudrock.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "cloudrock.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "cloudrock.labels" -}}
app.kubernetes.io/name: {{ include "cloudrock.name" . }}
helm.sh/chart: {{ include "cloudrock.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Set postgres version
*/}}
{{- define "cloudrock.postgresql.version" -}}
12
{{- end -}}

{{/*
Set postgres host
*/}}
{{- define "cloudrock.postgresql.host" -}}
{{- if .Values.postgresql.HAEnabled -}}
"postgresql-ha-cloudrock-pgpool"
{{- else -}}
"postgresql-cloudrock"
{{- end -}}
{{- end -}}

{{/*
Set postgres port
*/}}
{{- define "cloudrock.postgresql.port" -}}
"5432"
{{- end -}}

{{/*
Set postgres secret
*/}}
{{- define "cloudrock.postgresql.secret" -}}
{{- if .Values.postgresql.HAEnabled -}}
"postgresql-ha-cloudrock-postgresql"
{{- else -}}
"postgresql-cloudrock"
{{- end -}}
{{- end -}}

{{/*
Set postgres secret password key
*/}}
{{- define "cloudrock.postgresql.secret.passwordKey" -}}
"password"
{{- end -}}

{{/*
Set postgres database name
*/}}
{{- define "cloudrock.postgresql.dbname" -}}
{{ .Values.postgresql.database | quote }}
{{- end -}}

{{/*
Set postgres user
*/}}
{{- define "cloudrock.postgresql.user" -}}
{{ .Values.postgresql.username | quote }}
{{- end -}}

{{/*
Set rabbitmq host
*/}}
{{- define "cloudrock.rabbitmq.host" -}}
{{ printf "%s-rabbitmq-ha" .Values.rabbitmq.hostPrefix }}
{{- end -}}

{{/*
Set rabbitmq URL
*/}}
{{- define "cloudrock.rabbitmq.rmqUrl" -}}
{{ printf "amqp://%s:%s@%s:%d" .Values.rabbitmq.user .Values.rabbitmq.password .Values.rabbitmq.host (default 5672 .Values.rabbitmq.customAMQPPort) }}
{{- end -}}
