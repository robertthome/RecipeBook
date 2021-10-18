import axios from 'axios'

const Client = axios.create({
  baseURL:
    process.env.NODE_ENV === 'production'
      ? process.env.VUE_APP_API_URL
      : 'http://localhost:5000'
})
console.log(process.env.VUE_APP_API_URL)
export default Client
