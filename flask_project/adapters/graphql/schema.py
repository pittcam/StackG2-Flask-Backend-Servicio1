type_defs = """
type Query {
 _empty: String
}
type User {
  id: ID!
  email: String!
  username: String!
  name: String!
  token: String
}

type AuthResponse {
  id: ID!
  email: String!
  token: String!
}

type Mutation {
  registerUser(
    email: String!
    password: String!
    username: String!
    name: String!
  ): User
  
  loginUser(
    email: String!
    password: String!
  ): AuthResponse
}
"""
