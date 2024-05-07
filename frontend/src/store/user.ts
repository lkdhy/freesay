import {defineStore} from "pinia";

export const useUserstore = defineStore(
    'user',
    {
        state() {
            return {
                // initial: empty string
                userName: ''
            }
        }
    }
)