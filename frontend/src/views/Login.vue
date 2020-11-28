
<template>
    <div class="uk-child-width-expand@s uk-text-center uk-padding-large" uk-height-viewport="expand" uk-grid>
        <div>

        </div>
        <div>
            <form v-on:submit.prevent="validate">
                <fieldset class="uk-fieldset">
                    <legend class="uk-legend">Inloggen</legend>
                    
                    <div class="uk-margin">
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: user"></span>
                            <input 
                                class="uk-input uk-form-width-large" 
                                type="text" 
                                placeholder="Gebruikersnaam"
                                v-model="username">
                        </div>
                    </div>
                    <div class="uk-margin">
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: lock"></span>
                            <input 
                                class="uk-input uk-form-width-large" 
                                type="password" 
                                name="password" 
                                placeholder="Wachtwoord"
                                v-model="password">
                        </div>
                    </div>
                    <div class="uk-margin">
                         <button class="uk-button uk-form-width-large uk-button-primary">
                            <span v-if="!loading">Inloggen</span>
                            <span v-if="loading">
                                <div uk-spinner></div>
                            </span>
                        </button>
                    </div>
                </fieldset>
            </form>
        </div>
        <div>

        </div>
    </div>
</template>

<script lang="ts">

    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import VueRouter, { Route } from 'vue-router';

    import LoginService from '../services/LoginService';
    import DataService from '../services/DataService';
    import { User } from '../models/User';
    
    @Component
    export default class Login extends Vue {
        private username = '';
        private password = '';
        private loading = false;
      
        private validate(): void {
            this.loading = true;
            try {
                LoginService.authenticateUser(this.username, this.password).then(response => {
                    if(response.status === 200){
                        this.loading = false;
                        
                        const user: User = {
                            id: response.data.id, 
                            username: response.data.username 
                        };
                        
                        DataService.setData(user);
                        this.$router.push("/dashboard");
                    } 
                });
            } finally {
                this.loading = false;
            }
        }
        
    }
    
</script>
