<template>

    <button @click="deleteUser" class="rounded bg-blue-200">Test Delete User</button>
    <label for="shouldDeleteContent">Should delete content?</label>
    <input type="checkbox" v-model="shouldDeleteContent"/>

</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
    name: "SettingsView",
    data() {
        return {
            shouldDeleteContent: false
        }
    },
    methods: {
        deleteUser() {
            axiosClient.delete('/settings/delete_account/', {
                data: {
                    'should_delete_content': this.shouldDeleteContent
                }
            }).then(response => {
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