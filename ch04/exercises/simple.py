article = "The government of Finland will 'significantly' restrict the right of Russian citizens to enter the country as tourists or as transit when traveling to other parts of the Schengen area, the Finnish government said in a statement on Wednesday. 'Tomorrow, on Thursday 29 September, the Government will adopt a resolution that will significantly restrict the right of Russian citizens to enter Finland as tourists and to use Finland as a transit country when travelling to other parts of the Schengen area, as described in more detail in the resolution,' a statement from the government reads."

Dictionary = {
  "government":"HQ",
  "Government":"HQ",
  "Russian":"the Bear People's",
  "Russia":"the Land of Bears",
  "Finnish":"Unicorn People's",
  "Finland":"the Land of the Unicorns"
}
for key, value in Dictionary.items():
  article = article.replace(key, value)
print(article)