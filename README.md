# Investor Outreach Automation

This project is an automation script for reaching out to investors. It uses OpenAI's GPT-3 model to generate personalized emails to each investor based on their investment history.

## Setup

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Replace `'YOUR_API_KEY'` in `main.py` with your OpenAI API key.

## Usage

Run the script by executing `python main.py --file investors.csv --temperature 0.5 --max_tokens 200 --mode 'turing'`.

## Parameters

- `--file`: The CSV file containing the investors information.
- `--temperature`: The temperature for the GPT-3 model.
- `--max_tokens`: The maximum number of tokens for the GPT-3 model.
- `--mode`: The mode for the GPT-3 model.

## CSV File Format

The CSV file should contain the following columns:

- `Name`: The name of the investor.
- `Company Name`: The name of the company the investor is associated with.
- `Email`: The email address of the investor.
- `Investments`: A list of companies the investor has invested in.

## Email Format

The email sent to each investor will be personalized based on their investment history. The email will contain a proposal for them to consider investing in your company.

## Follow Up Emails

If the investor does not respond to the initial email, a follow up email will be sent after 5 days.

## Rate Limiting

The script handles rate limiting by OpenAI. If the rate limit is reached, the script will skip the current investor and move on to the next one.

## Logging

The script logs all actions, including the sending of emails and any errors that occur.