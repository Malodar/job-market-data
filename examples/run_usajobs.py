"""Run the usajobs-scraper Actor and print the rows. Needs an Apify account.

    pip install apify-client
    set APIFY_TOKEN from https://console.apify.com/settings/integrations
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("artsiom_k/usajobs-scraper").call(run_input={"keyword": "nurse", "includeDetails": True, "maxItems": 100, "mode": "full"})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
