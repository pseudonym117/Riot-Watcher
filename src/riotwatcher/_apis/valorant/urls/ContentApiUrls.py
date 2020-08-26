from .ValEndpoint import ValEndpoint


class ContentApiUrls:
    contents = ValEndpoint("/content/v1/contents", locale=str)
