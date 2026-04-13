K8S_CONTEXT ?= psdm-dev
PSWEB_KRBSECRET_PATH ?= secret/lcls/psdm/psdm-datamgr/psweb/krbkeytab
CALIBDB_URL_SECRET_PATH ?= secret/lcls/psdm/dev/calibdb/mongo
ROLEDB_URL_SECRET_PATH ?= secret/lcls/psdm/dev/roledb/mongo


.PHONY: ensure-context
ensure-context:
	@kubectl config use-context ${K8S_CONTEXT}

secrets:
	mkdir -p etc/.secrets/
	vault kv get -field=krbkeytab $(PSWEB_KRBSECRET_PATH) | base64 --decode --ignore-garbage > etc/.secrets/keytab
	vault kv get -field=calibdb_url $(CALIBDB_URL_SECRET_PATH)  > etc/.secrets/calibdb_url
	vault kv get -field=roledb_url $(ROLEDB_URL_SECRET_PATH) > etc/.secrets/roledb_url

clean-secrets:
	rm -rf etc/

run-apply:
	kubectl apply -k .

apply: ensure-context secrets run-apply clean-secrets

run-delete:
	kubectl delete -k .

delete: ensure-context secrets run-delete clean-secrets

run-dump:
	kubectl kustomize .

dump: ensure-context secrets run-dump clean-secrets

