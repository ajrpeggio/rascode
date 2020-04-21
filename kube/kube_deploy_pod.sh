#!/bin/bash

kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1

kubectl get pods

kubectl enable prometheus storage

kubectl stop

kubectl start