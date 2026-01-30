def retry_click(page, selector, retries=3):
    for _ in range(retries):
        try:
            page.click(selector)
            return
        except:
            page.wait_for_timeout(300)
    raise Exception(f"Failed to click {selector}")
