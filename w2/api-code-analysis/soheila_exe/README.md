# Newyork times information
  Get information from the New York Times
## API documentation
   You must obtain a valid API key to access the data to make API calls. Please create an account on the website: "https://api.nytimes.com."
   There is a default API key available for testing purposes.

### Get information about a specific data: "Apollo 11"
    How to call web service:
    url: https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Data&api-key=API_KEY
    parameters :
      q : "Apollo 11"
      api-key: ecmEGhTeFYvTGEAWcYZ6KJGmW6jrOjy0

    Response:
      Success:
        - Return specific data
      Unauthorized, invalid "api-key":
        - The "api-key" is invalid
      Invalid URL:
        - Using an invalid URL. There is something wrong with the URL.
    
          
      
    
   
