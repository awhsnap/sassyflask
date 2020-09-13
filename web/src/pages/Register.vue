<template>
  <Layout>
    <h1>Create an account</h1>
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" />
    <label for="password">Password:</label>
    <input type="text" name="password" id="password" />
    <label for="cpassword">Confirm Password:</label>
    <input type="text" name="cpassword" id="cpassword" />
    <label for="email">Email:</label>
    <input type="text" name="password" id="password" />
    <input type="button" value="submit">
  </Layout>
</template>

<script>
export default {
  metaInfo: {
    title: 'Login Logout Page'
  }
}
</script>
