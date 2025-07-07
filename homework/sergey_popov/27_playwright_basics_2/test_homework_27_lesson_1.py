from playwright.sync_api import Page, expect, Dialog


def test_window_alert(page: Page):
    def alert_ok(alert: Dialog):
        alert.accept()

    page.on('dialog', alert_ok)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('[class="a-button"]').click()
    loc_ok = page.locator('#result-text')
    expect(loc_ok).to_have_text('Ok')
