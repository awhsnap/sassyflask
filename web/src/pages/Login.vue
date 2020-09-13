<template>
  <Layout>
    <h1>Please Login To Continue</h1>
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" />
    <label for="username">Password:</label>
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
