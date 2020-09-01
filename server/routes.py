import webapp2
# This is the place where all of your URL mapping goes
route_list = []

# report urls
route_list.extend([
    webapp2.Route(r'/', handler='handlers.MainPage', methods="GET"),

])