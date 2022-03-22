# okta-expire-users

Simple python script to expire passwords and delete user sesssions for every user in an Okta organisation

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