# okta-expire-users

## Summary
Simple python script to expire passwords and delete user sesssions for every user in an Okta organisation

## Classification
[![Confidentiality](https://img.shields.io/badge/confidentiality-C1_(Public)-green?style=plastic)](https://adahealth.atlassian.net/wiki/spaces/IS/pages/808171/ISMS+Policy+2.+Information+Classification+and+Handling#5.1.3.-Confidentiality)

## Requirements

- python >= 3.9.1

## Usage

Set OKTA_URL and OKTA_API_KEY as environment variables in your shell

```bash
export OKTA_URL=<yourdomain.okta.com>
export OKTA_API_KEY=<your-api-token>
```
Run the script

```bash
python main.py
```
