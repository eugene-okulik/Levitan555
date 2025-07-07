from playwright.sync_api import Page, expect


def test_change_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_color = page.locator('#colorChange')
    if expect(button_color).to_have_css('color', 'rgb(220, 53, 69)'):
        button_color.click()
