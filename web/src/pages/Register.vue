<template>
  <Layout>
    <h1>Create an account</h1>
    <form @submit.prevent="processForm" method="post">
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" v-model="username" />
    <label for="password">Password:</label>
    <input type="text" name="password" id="password" v-model="password" />
    <label for="cpassword">Confirm Password:</label>
    <input type="text" name="cpassword" id="cpassword" />
    <label for="email">Email:</label>
    <input type="text" name="email" id="email" v-model="email"/>
    <input type="button" value="submit">
    </form>
  </Layout>
</template>

<script>
import axios from 'axios'
export default {

  data(){
    return {
        user: [],
        createUserForm: {
          username:'',
          password:'',
          email:''
        }
      
    }
  },
  methods: {
    submit (){
      const path = 'http://localhost:5000/user/register'
      axios.post(path, payload)
    }
  },
  metaInfo: {
    title: 'Create an Account'
  }
}
</script>
