<template v-if="render" class="transition">
    <div class="bg-pink-50 dark:bg-gray-900 h-full md:px-10 pb-20">
        <div class="min-h-screen">
            <div class="flex items-center mb-1 md:px-10 px-3 py-10">
                <br><br>
                <h1 class="text-5xl font-bold">Settings</h1>
            </div>
            <div class="flex border-gray-200 md:px-9 px-4 gap-1 mb-6 rounded-md flex-wrap">
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset  shadow-[2px_2px_0px_0px_#000000] focus:ring-4  focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'my-details', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'my-details' }"
                        @click="activeTab = 'my-details'"
                >
                    My Details
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset shadow-[2px_2px_0px_0px_#000000] focus:ring-4 focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'password', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'password' }"
                        @click="activeTab = 'password'"
                >
                    Password
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset  shadow-[2px_2px_0px_0px_#000000] focus:ring-4  focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'preference', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'preference' }"
                        @click="activeTab = 'preference'"
                >
                    Preference
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset  shadow-[2px_2px_0px_0px_#000000] focus:ring-4  focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'accessibility', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'accessibility' }"
                        @click="activeTab = 'accessibility'"
                >
                    Accessibility
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset dark:shadow-[2px_2px_0px_0px_#ffffff] shadow-[2px_2px_0px_0px_#000000] focus:ring-4 focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        @click="logout"
                >
                    Logout
                </button>
            </div>
            <div v-if="activeTab === 'my-details'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-2">My Details</h2>
                <br>
                <form>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="name">
                            Name:
                        </label>
                        <p class="font-medium mb-2">{{ user_fullname }}</p>
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="email">
                            Email
                        </label>
                        <p class="italic mb-2"> {{ user_email }} </p>
                    </div>
                    <button @click="toggleForm"
                            class="transition focus:ring-4 focus:ring-pink-400 mb-4 bg-blue-500 hover:bg-blue-700 focus:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            type="button"
                    >
                        Edit Name
                    </button>
                    <div v-show="showForm">
                        <div class="mb-4">
                            <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="first-name">
                                First Name
                            </label>
                            <input
                                    class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 text-gray-700 dark:text-gray-200 hover:bg-gray-100 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                    v-model="first_name"
                                    type="text"
                                    placeholder="Enter first name"
                            />
                        </div>
                        <div class="mb-4">
                            <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="last-name">
                                Last Name
                            </label>
                            <input
                                    class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 text-gray-700 dark:text-gray-200 hover:bg-gray-100 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                    v-model="last_name"
                                    type="text"
                                    placeholder="Enter last name"
                            />
                        </div>
                        <button :disabled="isNameFormComplete" v-on:click="changeName"
                                class="transition focus:ring-4  focus:ring-pink-400 bg-blue-500 hover:bg-blue-700 focus:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                                type="submit"
                        >
                            Save Changes
                        </button>
                    </div>
                    <label v-if="success" class="text-green-600 pl-4">{{ successMessageName }}</label>
                    <label v-if="invalid" class="text-red-600 pl-4">{{ errorMessageName }}</label>
                </form>
                <button @click="deleteUser"
                        class="transition focus:ring-4 focus:ring-pink-400 mb-4 bg-red-500 hover:bg-red-700 focus:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                        type="button"
                >
                    Delete Account
                </button>
            </div>
            <div v-if="activeTab === 'password'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-4">Change Password</h2>
                <form @submit.prevent="submitForm">
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="current-password">
                            Current Password
                        </label>
                        <input
                                class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 text-gray-700 dark:text-gray-200 hover:bg-gray-100 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                v-model="old_password"
                                type="password"
                                placeholder="********"
                        />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="new-password">
                            New Password
                        </label>
                        <input
                                class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 hover:bg-gray-100 text-gray-700 dark:text-gray-200 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                v-model="new_password"
                                type="password"
                                placeholder="********"
                        />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="confirm-password">
                            Confirm New Password
                        </label>
                        <input
                                class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 hover:bg-gray-100 text-gray-700 dark:text-gray-200 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                v-model="conf_password"
                                type="password"
                                placeholder="********"
                        />
                    </div>
                    <div class="flex items-center justify-between">
                        <button :disabled="isFormComplete"
                                class="transition focus:ring-4  focus:ring-pink-400 bg-blue-500 hover:bg-blue-700 focus:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                                type="submit"
                        >
                            Save Changes
                        </button>
                        <label v-if="success" class="text-green-600 pl-4">{{ successMessage }}</label>
                        <label v-if="invalid" class="text-red-600 pl-4">{{ errorMessage }}</label>
                    </div>
                </form>
            </div>

            <div v-if="activeTab === 'preference'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-4">Preference Settings</h2>
                <form>
                    <!--                    <div class="mb-4">-->
                    <!--                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="notification-toggle">-->
                    <!--                            Receive Notifications-->
                    <!--                        </label>-->
                    <!--                        <input class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 mr-2 leading-tight " type="checkbox" id="notification-toggle">-->
                    <!--                        <label class="text-sm text-gray-700 dark:text-gray-200" for="notification-toggle">-->
                    <!--                            Enable email notifications for new messages-->
                    <!--                        </label>-->
                    <!--                    </div>-->
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="theme-select">
                            Theme
                        </label>
                        <div class="relative">
                            <select
                                    class="block transition focus:ring-4 focus:outline-none focus:ring-blue-400 appearance-none w-full bg-white dark:bg-black border border-gray-400 dark:border-gray-600 focus:bg-gray-100 dark:focus:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-800 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
                                    id="theme-select" v-model="themeSelect">
                                <option value="default">Default</option>
                                <option value="dark">Dark</option>
                                <option value="light">Light</option>
                            </select>
                            <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700 dark:text-gray-200">
                                <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg"
                                     viewBox="0 0 20 20">
                                    <path
                                            d="M14.707 7.293a1 1 0 0 0-1.414 0L10 10.586 6.707 7.293a1 1 0 1 0-1.414 1.414l3 3a1 1 0 0 0 1.414 0l3-3a1 1 0 0 0 0-1.414z"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <button
                            class="transition focus:ring-4 focus:ring-pink-400 bg-blue-500 focus:bg-blue-700 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                            type="button" v-on:click="changeTheme">
                        Save Settings
                    </button>
                </form>
            </div>

            <div v-if="activeTab === 'accessibility'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-4">Accessibility Options</h2>
                <p class="mb-2">Adjust the following settings to enhance the accessibility of this website:</p>
                <br>
                <div class=" rounded-lg md:px-16 px-5 py-8 mb-3  border-2 border-black bg-white dark:bg-gray-800 ">
                    <div class="mb-6">Keyboard shortcuts</div>
                    <div class="flex flex-wrap gap-1">
                      <ul>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">h</kbd> to return home</li>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">k</kbd> to search</li>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">m</kbd> to jump to module bar</li>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">q</kbd> to ask a question on a module specific page</li>


                      </ul>
                    </div>
                </div>
                <div class=" rounded-lg md:px-16 px-5 py-8 mb-3  border-2 border-black bg-white dark:bg-gray-800 ">
                    <div class="mb-6">Text adjustments</div>
                    <div class="flex flex-wrap gap-1">
                        <button v-on:click="toggleFont"
                                :class="{ 'bg-blue-500 hover:bg-blue-400 ': readableFont, 'hover:shadow-blue-200 hover:bg-sky-50 dark:hover:bg-transparent dark:hover:shadow-blue-600' : !readableFont}"
                                class="focus:outline-none overflow-hidden relative transition hover:shadow-lg hover:shadow-blue-600 hover:-translate-y-1 group rounded h-[200px] w-[400px] focus:ring-4 focus:ring-pink-400 border-2 border-blue-500">
                            <div :class="{ 'text-white bg-black bg-opacity-10': readableFont, 'text-blue-500 bg-white bg-opacity-30 dark:bg-black dark:bg-opacity-30': !readableFont}"
                                 class=" overflow-auto absolute px-5 inset-0 py-7  backdrop-blur-lg delay-700 opacity-0 duration-500 group-focus:opacity-100 group-hover:opacity-100">
                                <span>Current font: Lorem ipsum dolor sit amet, <span class="font-bold">consectetur adipiscing</span> elit. Duis <span
                                        class=" italic">placerat</span> ut justo.</span><br><br><span
                                    class="font-[helvetica]">Readable font: Lorem ipsum dolor sit amet, <span
                                    class="font-bold">consectetur adipiscing</span> elit. Duis <span class="italic">placerat</span> ut justo.</span>
                            </div>
                            <div class="flex justify-center gap-4">
                                <div :class="{ 'text-white': readableFont, 'text-blue-500': !readableFont}"
                                     class=" text-7xl">Aa
                                </div>
                                <div :class="{ 'text-white': readableFont, 'text-blue-500': !readableFont}"
                                     class=" text-center align-middle self-center">Readable font
                                </div>
                            </div>
                        </button>
                        <button v-on:click="toggleLargeFontSize"
                                :class="{ 'bg-blue-500 hover:bg-blue-400 ': largeFontSize, 'hover:shadow-blue-200 hover:bg-sky-50 dark:hover:bg-transparent dark:hover:shadow-blue-600' : !largeFontSize}"
                                class="transition  hover:shadow-lg hover:-translate-y-1 hover:shadow-blue-600 focus:outline-none focus:ring-4 focus:ring-pink-400 rounded  h-[200px] w-[200px]  border-2 border-blue-500">
                            <div class=" inline-block">
                                <svg :class="{ 'fill-white': largeFontSize, 'fill-blue-500': !largeFontSize}"
                                     class=" scale-[0.8]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                                    <!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                                    <path d="M64 128V96h64l0 320H96c-17.7 0-32 14.3-32 32s14.3 32 32 32H224c17.7 0 32-14.3 32-32s-14.3-32-32-32H192l0-320h64v32c0 17.7 14.3 32 32 32s32-14.3 32-32V80c0-26.5-21.5-48-48-48H160 48C21.5 32 0 53.5 0 80v48c0 17.7 14.3 32 32 32s32-14.3 32-32zM502.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-64 64c-9.2 9.2-11.9 22.9-6.9 34.9s16.6 19.8 29.6 19.8h32V352H416c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9l64 64c12.5 12.5 32.8 12.5 45.3 0l64-64c9.2-9.2 11.9-22.9 6.9-34.9s-16.6-19.8-29.6-19.8H512V160h32c12.9 0 24.6-7.8 29.6-19.8s2.2-25.7-6.9-34.9l-64-64z"/>
                                </svg>
                                <div :class="{ 'text-white': largeFontSize, 'text-blue-500': !largeFontSize}"
                                     class="text-center">Large font size
                                </div>
                            </div>
                        </button>
                        <button v-on:click="changeLetterSpacing"
                                :class="{'hover:shadow-blue-200 hover:bg-sky-50 dark:hover:bg-transparent dark:hover:shadow-blue-600' : true}"
                                class="transition  hover:shadow-lg hover:-translate-y-1 hover:shadow-blue-600 focus:outline-none focus:ring-4 focus:ring-pink-400 rounded  h-[200px] w-[200px]  border-2 border-blue-500">
                            <div class=" inline-block">
                                <svg :class="{'fill-blue-500': true, 'scale-[0.54]': currentLetterSpacing == 'normal','-translate-y-1': currentLetterSpacing == 'normal' && largeFontSize}"
                                     class=" scale-[0.6] translate-x-2" xmlns="http://www.w3.org/2000/svg"
                                     viewBox="0 0 576 512">
                                    <!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
                                    <path d="M64 128V96H192l0 128H176c-17.7 0-32 14.3-32 32s14.3 32 32 32h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H256l0-128H384v32c0 17.7 14.3 32 32 32s32-14.3 32-32V80c0-26.5-21.5-48-48-48H224 48C21.5 32 0 53.5 0 80v48c0 17.7 14.3 32 32 32s32-14.3 32-32zM9.4 361.4c-12.5 12.5-12.5 32.8 0 45.3l64 64c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6V416H320v32c0 12.9 7.8 24.6 19.8 29.6s25.7 2.2 34.9-6.9l64-64c12.5-12.5 12.5-32.8 0-45.3l-64-64c-9.2-9.2-22.9-11.9-34.9-6.9s-19.8 16.6-19.8 29.6v32H128V320c0-12.9-7.8-24.6-19.8-29.6s-25.7-2.2-34.9 6.9l-64 64z"/>
                                </svg>
                                <div :class="{'text-blue-500': true,'-translate-y-4' : !largeFontSize && currentLetterSpacing != 'normal', '-translate-y-9' : largeFontSize && currentLetterSpacing == 'normal'}"
                                     class="text-center -translate-y-6">Letter spacing: <span
                                        class="font-semibold">{{ currentLetterSpacing }}</span></div>
                            </div>
                        </button>
                    </div>
                </div>
                
                <div class=" rounded-lg md:px-16 px-5 py-6  border-2 border-black bg-white dark:bg-gray-800 ">
                    <div class="mb-6">Colour adjustments</div>
                    <div class="flex flex-wrap gap-1">
                        <button v-on:click="toggleGrayscale"
                                :class="{ 'bg-blue-500 hover:bg-blue-400 ': grayscaleMode, 'hover:shadow-blue-200 hover:bg-sky-50 dark:hover:bg-transparent dark:hover:shadow-blue-600' : !grayscaleMode}"
                                class="transition hover:shadow-lg hover:-translate-y-1 hover:shadow-blue-600 focus:outline-none focus:ring-4 focus:ring-pink-400 rounded relative h-[200px] w-[200px]  border-2 border-blue-500">
                            <div class=" block">
                                <div class="text-7xl mb-5">🗿</div>
                                <div :class="{ 'text-white': grayscaleMode, 'text-blue-500': !grayscaleMode}"
                                     class="text-center">Grayscale mode
                                </div>
                            </div>
                        </button>
                        <button v-on:click="toggleInvert"
                                :class="{ 'bg-blue-500 hover:bg-blue-400 ': invert, 'hover:shadow-blue-200 hover:bg-sky-50 dark:hover:bg-transparent dark:hover:shadow-blue-600' : !invert}"
                                class="transition hover:shadow-lg hover:-translate-y-1 hover:shadow-blue-600 focus:outline-none focus:ring-4 focus:ring-pink-400 rounded relative h-[200px] w-[200px]  border-2 border-blue-500">
                            <div class="block">
                                <div :class="{ 'text-white': invert, 'text-blue-500': !invert}" class="text-8xl">⥃</div>
                                <div :class="{ 'text-white': invert, 'text-blue-500': !invert}"
                                     class="text-center mt-1 pb-2">Invert colour
                                </div>
                            </div>
                        </button>
                        <button class=" cursor-default focus:outline-none focus:ring-4 focus:ring-pink-400 hover:shadow-blue-200 hover:bg-sky-50 hover:shadow-lg hover:-translate-y-1 dark:hover:bg-transparent dark:hover:shadow-blue-600 border-blue-500 rounded justify-center h-[200px] w-[400px] col-span-2 border-2">
                            <div class="flex justify-center -translate-x-2">
                                <div class="text-7xl">🎨</div>
                                <div class="flex flex-col pt-4">
                                    <div class="flex gap-1 justify-center">
                                        <button v-on:click="changeHue(-30)"
                                                class="transition focus:ring-4 focus:ring-pink-400 focus:outline-none hover:bg-blue-400 font-bold rounded-md h-8 w-8 bg-blue-500 text-center text-white">
                                            -
                                        </button>
                                        <div class=" flex flex-col w-16 rounded-md dark:bg-gray-600 bg-blue-50 text-center justify-center">
                                            <label class="font-medium dark:text-sky-100 text-blue-800">{{
                                                colourHue
                                                }}°</label></div>
                                        <button v-on:click="changeHue(30)"
                                                class="transition focus:ring-4 focus:ring-pink-400 focus:outline-none hover:bg-blue-400 font-bold rounded-md  h-8 w-8 bg-blue-500 text-center text-white">
                                            +
                                        </button>
                                    </div>
                                    <div class="text-center text-blue-500 mt-1">Shift colour hue</div>
                                </div>
                            </div>
                        </button>
                    </div>
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
            first_name: '',
            last_name: '',
            user_fullname: '',
            user_email: '',
            old_password: '',
            new_password: '',
            conf_password: '',
            success: false,
            successName: false,
            successMessageName: '',
            successMessage: '',
            errorMessage: '',
            errorMessageName: '',
            invalidName: false,
            invalid: false,
            largeFontSize: localStorage.getItem("largeFont") === "true",
            readableFont: localStorage.getItem("readableFont") === "true",
            grayscaleMode: localStorage.getItem("grayscale") === "true",
            invert: localStorage.getItem("invert") === "true",
            colourHue: Number(localStorage.getItem("colourHue")) || 0,
            letterSpacing: ['tight', 'normal', 'wide'],
            currentLetterSpacing: localStorage.getItem("letterSpacing") || 'normal',
            highContrastMode: false,
            screenReaderMode: false,
            themeSelect: localStorage.getItem("theme") || "default",
            pageReload: localStorage.getItem("pageReload"),
            render: true,
            showForm: false,

        }
    },
    methods: {
        largeFontIcon(largeFontSize) {
            if (largeFontSize) {
                return "color: white;"
            } else {
                return "color: #3b82f6;"
            }
        },
        changeName() {
            axiosClient.post('/settings/change_username/', {
                first_name: this.first_name,
                last_name: this.last_name,
            })
                .then((response) => {
                    console.log(response);
                    this.successName = true
                    this.invalidName = false
                    this.successMessageName = "Username successfully changed!"
                })
                .catch((error) => {
                    console.log(error);
                    this.successName = false
                    this.invalidName = true
                    this.errorMessageName = "Unable to change username"
                    this.textInput = "border-2 p-2 w-full rounded text-gray-700 dark:text-gray-200 focus:outline-none focus:ring-2 focus:ring-red-100 border-red-500"
                });
        },
        changeTheme() {
            document.body.classList.remove("light", "dark", "default")
            localStorage.setItem("theme", this.themeSelect || "default")
            document.body.classList.add(this.themeSelect || "default")
            //window.location.reload()
            this.render = false
            this.render = true
        },
        toggleLargeFontSize() {
            this.largeFontSize = !this.largeFontSize
            localStorage.setItem("largeFont", this.largeFontSize)
            localStorage.setItem("pageReload", true)
            setTimeout(function () {
                window.location.reload()
            }, 155)
        },
        toggleFont() {
            document.body.classList.remove(this.readableFont ? 'font-[sans-serif]' : 'font-sans')
            this.readableFont = !this.readableFont
            localStorage.setItem("readableFont", this.readableFont)
            document.body.classList.add(this.readableFont ? 'font-[sans-serif]' : 'font-sans')
            this.render = false
            this.render = true
        },
        toggleForm() {
            this.showForm = !this.showForm
        },
        toggleGrayscale() {
            document.body.classList.remove('grayscale')
            this.grayscaleMode = !this.grayscaleMode
            localStorage.setItem("grayscale", this.grayscaleMode)
            document.body.classList.add(this.grayscaleMode ? 'grayscale' : '')
            this.render = false
            this.render = true
        },
        toggleInvert() {
            document.body.classList.remove('invert')
            this.invert = !this.invert
            localStorage.setItem("invert", this.invert)
            document.body.classList.add(this.invert ? 'invert' : '')
            this.render = false
            this.render = true
        },
        changeHue(hue) {
            document.body.classList.remove('hue-rotate-[' + localStorage.getItem("colourHue") + 'deg]')
            this.colourHue += hue
            this.colourHue = this.colourHue % 360
            localStorage.setItem("colourHue", this.colourHue)
            document.body.classList.add('hue-rotate-[' + localStorage.getItem("colourHue") + 'deg]')
            this.render = false
            this.render = true
        },
        changeLetterSpacing() {
            document.body.classList.remove('tracking-' + localStorage.getItem("letterSpacing"))
            var current = this.letterSpacing.indexOf(localStorage.getItem("letterSpacing") || 1)
            localStorage.setItem("letterSpacing", this.currentLetterSpacing = this.letterSpacing[(current + 1) % 3])
            document.querySelectorAll('.tracking-tight').forEach(e => e.classList.remove('tracking-tight'));
            document.body.classList.add('tracking-' + localStorage.getItem("letterSpacing"))

        },
        logout() {
            axiosClient.post('/v1/token/logout/')
                .then(response => {

                    this.$store.commit('removeToken')

                    axiosClient.defaults.headers.common['Authorization'] = ""
                    localStorage.setItem("token", "")
                    this.$router.push('/log-in/')
                })
                .catch(error => {
                    console.log(error)
                })
        },
        deleteUser() {
            // ask if user want to delete all content as well
            if (window.confirm("Do you want to delete all your content as well?")) {
                this.shouldDeleteContent = true
            } else {
                this.shouldDeleteContent = false
            }

            if (window.prompt("Are you sure you want to delete your account? Type 'DELETE' to confirm.").toUpperCase() !== "DELETE") {
                return
            }

            axiosClient.delete('/settings/delete_account/', {
                data: {
                    'should_delete_content': this.shouldDeleteContent
                }
            }).then(response => {
                console.log(response)
                this.$store.commit('removeToken')
                axiosClient.defaults.headers.common['Authorization'] = ""
                localStorage.setItem("token", "")
                this.$router.push('/log-in/')
            }).catch(error => {
                console.log(error)
            })
        },
        submitForm(e) {
            const formData = {
                new_password: this.new_password,
                re_new_password: this.conf_password,
                current_password: this.old_password,
            }

            axiosClient.post('/v1/users/set_password/', formData)
                .then(response => {
                    console.log(response)

                    this.success = true
                    this.invalid = false
                    this.successMessage = "Password successfully changed!"
                })
                .catch(error => {
                    console.log(error)
                    if (error.response.status === 400) {
                        this.errorMessage = "Invalid password"
                    } else {
                        //set this.errorMessage to the first element of the only attribute of error.response.data
                        this.errorMessage = Object.values(error.response.data)[0][0]
                    }
                    this.invalid = true
                    this.success = false
                    this.textInput = "border-2 p-2 w-full rounded text-gray-700 dark:text-gray-200 focus:outline-none focus:ring-2 focus:ring-red-100 border-red-500"
                })

        },
    },
    computed: {
        isFormComplete() {
            return (this.old_password === '') || (this.new_password === '') || (this.conf_password === '');
        },
        isNameFormComplete() {
            return (this.first_name === '') || (this.last_name === '');
        }
    },
    mounted() {
        document.body.classList.add('transition')
        if (this.pageReload == 'true') {
            this.activeTab = 'accessibility'
            localStorage.setItem("pageReload", false)
        }

        axiosClient.get("home_page/user_prof").then((response) => {
            this.user = response.data;
            this.user_fullname = response.data.full_name;
            this.user_email = response.data.username;
        })
    }
}
</script>

<style scoped>

</style>
