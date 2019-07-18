#!/usr/bin/env bash

curl -X POST --data "{\"username\":\"test\"}" -H "Content-Type: application/json" localhost:6543/register
