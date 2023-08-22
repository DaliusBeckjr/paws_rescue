APIKey = '0PhFtnE2nmvzUVyCKewIVvqKRv7ZpJkEXSr8Yf5h';
SECRETKey = '0PhFtnE2nmvzUVyCKewIVvqKRv7ZpJkEXSr8Yf5h';




async function bearToken_call() {
    let url = 'https://api.petfinder.com/v2/oauth2/token';
    let options = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `grant_type=client_credentials&client_id=${APIKey}&client_secret=${SECRETKey}`
    };

    let response = await fetch(url, options);
    let jsonData = await response.json();
    console.log(jsonData)
}

bearToken_call()
