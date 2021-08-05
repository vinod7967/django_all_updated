from django.shortcuts import HttpResponse
class BrtoherMiddleware:
 def __init__(self, get_response):
  self.get_response = get_response
  print("One Time Brtoher Initialization")

 def __call__(self, request):
  print("This is Brother before view")
  response = self.get_response(request)
  print("This is Brother after view")
  return response

class FatherMiddleware:
 def __init__(self, get_response):
  self.get_response = get_response
  print("One Time Father Initialization")

 def __call__(self, request):
  print("This is Father before view")
  response = self.get_response(request)
  # response = HttpResponse("Hi")
  print("This is Father after view")
  return response

class MummyMiddleware:
 def __init__(self, get_response):
  self.get_response = get_response
  print("One Time Mummy Initialization")

 def __call__(self, request):
  print("This is Mummy before view")
  response = self.get_response(request)
  print("This is Mummy after view")
  return response