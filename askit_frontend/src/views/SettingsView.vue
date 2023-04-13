<template>

  <button @click="deleteUser">Test Delete User</button>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
    name: "SettingsView",
    methods: {
        deleteUser() {
            axiosClient.delete('/api/settings/delete_user/').then(response => {
                console.log(response)
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>

</style>