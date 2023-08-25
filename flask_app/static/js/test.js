// API Key - zPtAtBdN
// go here for more information on the api https://test1-api.rescuegroups.org/v5/public/docs

// our fetch example from vue.js maybe try to figure out how to retrieve the data 
// from this api while changing the interface. doesn't need a bearer token but a api
// key to access the information
// async Register() {
//     const path = 'http://localhost:8000/register'
//     const options = {
//         method: "POST",
//         headers: {
//             Accept: "application/json",
//             "Content-Type": "application/json;charset=UTF-8",
//         },
//         body: JSON.stringify({
//             email: this.email,
//             password: this.password,
//         }),
//     };
//     const response = await fetch(path, options);
//     let data = response.json()

// link for a better starter reference https://blog.logrocket.com/axios-vs-fetch-best-http-requests/#basic-syntax

// fetchData() {
//     const path = "http://localhost:8000/ping";
//     fetch(path, {method:"GET"})
//     .then(response => response.json() )
//     .then(data => {
//         console.log(data)  //this will display data in our console
//         this.msg = data
//     })
//     .catch(err => console.log(err.message))
// }
// },

// note: lets also try to add a try and catch to it kinda like this one and figure out some more stuff. this is in vue.js framework btw so its rough 