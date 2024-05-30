import {defineStore} from "pinia";

export const useUserstore = defineStore(
    'user',
    {
        state() {
            return {
                // initial: empty string
                userName: '',
                avatar: '',
                signature: '',
                isAdmin: false,
                visitedUserName: ''
            }
        }
    }
)

export const useTagsStore = defineStore(
    'tags',
    {
        state() {
            return {
                tags: []
            }
        }
    }
)