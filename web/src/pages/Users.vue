<template>
  <Layout>
    <h1>User Management</h1>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error doloremque omnis animi, eligendi magni a voluptatum, vitae, consequuntur rerum illum odit fugit assumenda rem dolores inventore iste reprehenderit maxime! Iusto.</p>
    <ul>
      <li v-for="user in user">
        <li v-for="user in users.users">
          {{ user.username }} | {{user.email}}
        </li>
      </li>
    </ul>
  </Layout>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      users: {}
    }
  },
  async mounted () {
    try {
      const results = await axios.get(
        'http://localhost:5000/users'
      )

      this.users = results.data
    } catch (error) {
      this.users = {'message': 'Error'}
      console.log(error)
    }
  },
  metaInfo: {
    title: 'User Management'
  }
}


</script>
