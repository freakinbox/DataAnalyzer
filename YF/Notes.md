Yahoo Finance URLs should expire after a few days so I will have to manually make the lists for now and put them into the program to pull from the stocks profile instead.


soup.p = address




{"size":25,"offset":0,"sortField":"intradaymarketcap","sortType":"DESC","quoteType":"EQUITY","topOperator":"AND","query":{"operator":"AND","operands":[{"operator":"or","operands":[{"operator":"EQ","operands":["region","us"]}]},{"operator":"btwn","operands":["lastclosemarketcap.lasttwelvemonths",0,100000000]}]},"userId":"","userIdType":"guid"}



fetch("https://query1.finance.yahoo.com/v1/finance/screener/public/save?crumb=qaFzythCc3q&lang=en-CA&region=CA&corsDomain=ca.finance.yahoo.com", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  "referrer": "https://ca.finance.yahoo.com/screener/new",
  "referrerPolicy": "no-referrer-when-downgrade",
  "body": "{\"criteria\":{\"size\":25,\"offset\":0,\"sortField\":\"intradaymarketcap\",\"sortType\":\"DESC\",\"quoteType\":\"EQUITY\",\"topOperator\":\"AND\",\"query\":{\"operator\":\"AND\",\"operands\":[{\"operator\":\"or\",\"operands\":[{\"operator\":\"EQ\",\"operands\":[\"region\",\"ca\"]}]}]}}}",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
});