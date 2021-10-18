import Client from './api'

export const GetArticles = async () => {
  const res = await Client.get('/articles')
  return res.data
}

export const CreateArticle = async data => {
  const res = await Client.post('/articles', data)
  return res.data
}

export const DeleteArticle = async id => {
  const res = await Client.delete(`/articles/${id}`)
  return res
}
