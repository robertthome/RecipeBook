import axios from 'axios'

const Client = axios.create({
  baseURL:
    process.env.FLASK_ENV === 'production'
      ? process.env.VUE_APP_API_URL
      : 'http://localhost:5000'
})

export default Client
