<template>
  <div class="bg-pink-50">
    <div class="min-h-screen">
      <div class="flex items-center mb-1 px-10 py-10 ">
        <br><br>
        <h1 class="text-5xl font-bold">Settings</h1>
      </div>
      <div class="flex border-gray-200 px-9 mb-6">
        <button
            class="py-2 px-4 text-xl bg-white text-gray-700 border-b-2 rounded-md font-medium focus:outline-none focus:border-indigo-500 hover:border-indigo-500 mr-2"
            :class="{ 'border-indigo-500': activeTab === 'my-details' }"
            style="box-shadow: .13em .13em;"
            @click="activeTab = 'my-details'"
        >
          My Details
        </button>
        <button
            class="py-2 px-4 text-xl bg-white text-gray-700 border-b-2 rounded-md font-medium focus:outline-none focus:border-indigo-500 hover:border-indigo-500 mr-2"
            :class="{ 'border-indigo-500': activeTab === 'password' }"
            style="box-shadow: .13em .13em;"
            @click="activeTab = 'password'"
        >
          Password
        </button>
        <button
            class="py-2 px-4 text-xl bg-white text-gray-700 border-b-2 rounded-md font-medium focus:outline-none focus:border-indigo-500 hover:border-indigo-500 mr-2"
            :class="{ 'border-indigo-500': activeTab === 'preference' }"
            style="box-shadow: .13em .13em;"
            @click="activeTab = 'preference'"
        >
          Preference
        </button>
        <button
            class="py-2 px-4 text-xl bg-white text-gray-700 border-b-2 rounded-md font-medium focus:outline-none focus:border-indigo-500 hover:border-indigo-500 mr-2"
            :class="{ 'border-indigo-500': activeTab === 'accessibility' }"
            style="box-shadow: .13em .13em;"
            @click="activeTab = 'accessibility'"
        >
          Accessibility
        </button>
      </div>
      <div v-if="activeTab === 'my-details'" class="px-10">
        <h2 class="text-2xl font-bold mb-2">My Details</h2>
        <br>
        <form>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="name">
              Name:
            </label>
            <p class="font-medium mb-2">Student Name</p>
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="email">
              Email
            </label>
            <p class="italic mb-2"> student@xyz.com </p>
          </div>
        </form>
      </div>
      <div v-if="activeTab === 'password'" class="px-10">
        <h2 class="text-2xl font-bold mb-4">Change Password</h2>
        <form>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="current-password">
              Current Password
            </label>
            <input
                class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="current-password"
                type="password"
                placeholder="********"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="new-password">
              New Password
            </label>
            <input
                class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="new-password"
                type="password"
                placeholder="********"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="confirm-password">
              Confirm New Password
            </label>
            <input
                class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="confirm-password"
                type="password"
                placeholder="********"
            />
          </div>
          <div class="flex items-center justify-between">
            <button
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="button"
            >
              Save Changes
            </button>
          </div>
        </form>
      </div>

      <div v-if="activeTab === 'preference'" class="px-10">
        <h2 class="text-2xl font-bold mb-4">Preference Settings</h2>
        <form>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="notification-toggle">
              Receive Notifications
            </label>
            <input class="mr-2 leading-tight" type="checkbox" id="notification-toggle">
            <label class="text-sm text-gray-700" for="notification-toggle">
              Enable email notifications for new messages
            </label>
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-bold mb-2" for="theme-select">
              Theme
            </label>
            <div class="relative">
              <select
                  class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
                  id="theme-select">
                <option value="default">Default</option>
                <option value="dark">Dark</option>
                <option value="light">Light</option>
              </select>
              <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                  <path
                      d="M14.707 7.293a1 1 0 0 0-1.414 0L10 10.586 6.707 7.293a1 1 0 1 0-1.414 1.414l3 3a1 1 0 0 0 1.414 0l3-3a1 1 0 0 0 0-1.414z"/>
                </svg>
              </div>
            </div>
          </div>
          <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              type="submit">
            Save Settings
          </button>
        </form>
      </div>

      <div v-if="activeTab === 'accessibility'" class="px-10">
        <h2 class="text-2xl font-bold mb-4">Accessibility Options</h2>
        <p class="mb-2">Adjust the following settings to enhance the accessibility of this website:</p>
        <br>
        <div class="flex items-center mb-6">
          <label for="high-contrast-mode" class="mr-4">High Contrast Mode</label>
          <input type="checkbox" id="high-contrast-mode" class="mr-2" v-model="highContrastMode">
        </div>
        <div class="flex items-center mb-6">
          <label for="large-font-size" class="mr-4">Large Font Size</label>
          <input type="checkbox" id="large-font-size" class="mr-2" v-model="largeFontSize">
        </div>
        <div class="flex items-center mb-6">
          <label for="screen-reader-mode" class="mr-4">Screen Reader Mode</label>
          <input type="checkbox" id="screen-reader-mode" class="mr-2" v-model="screenReaderMode">
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
  name: "SettingsView",
  data() {
    return {
      activeTab: 'my-details', // Set the default active tab
      shouldDeleteContent: false,
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
