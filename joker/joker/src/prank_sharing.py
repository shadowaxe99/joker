import webbrowser

class PrankSharing:
    def __init__(self):
        pass

    def share_prank_on_facebook(self, prank):
        url = f'https://www.facebook.com/sharer/sharer.php?u={prank}'
        webbrowser.open(url)

    def share_prank_on_twitter(self, prank):
        url = f'https://twitter.com/intent/tweet?url={prank}'
        webbrowser.open(url)

    def share_prank_on_instagram(self, prank):
        url = f'https://www.instagram.com/?url={prank}'
        webbrowser.open(url)

    def share_prank_on_whatsapp(self, prank):
        url = f'https://api.whatsapp.com/send?text={prank}'
        webbrowser.open(url)