
<template>
    <div class="uk-flex uk-flex-center uk-margin-top">
        <form v-on:submit.prevent="validate">
            <fieldset class="uk-fieldset">
                <legend class="uk-legend">{{ this.status ? 'Inloggen' : 'Maak een account aan' }}</legend>
                
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
                 <div class="uk-margin" v-if="!status">
                    <div class="uk-inline">
                        <span class="uk-form-icon" uk-icon="icon: mail"></span>
                        <input 
                            class="uk-input uk-form-width-large" 
                            type="email" 
                            name="email" 
                            placeholder="E-mailadres"
                            v-model="email">
                    </div>
                </div>
                <div class="uk-margin" v-if="status">
                    <button class="uk-button uk-form-width-large uk-button-primary">
                        <span v-if="!loading">Inloggen</span>
                        <span v-if="loading">
                            <div uk-spinner></div>
                        </span>
                    </button>
                </div>
                <div class="uk-margin" v-if="!status">
                    <button class="uk-button uk-form-width-large uk-button-primary">
                        <span v-if="!loading">Maak een account aan</span>
                        <span v-if="loading">
                            <div uk-spinner></div>
                        </span>
                    </button>
                </div>
                <div class="uk-margin">
                    <a class="uk-link-muted" v-on:click="switchStatus">{{ this.status ? 'Maak een account aan' : 'Inloggen' }}</a>
                </div>
            </fieldset>
        </form>       
    </div>
</template>

<script lang="ts">

    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import VueRouter, { Route } from 'vue-router';
    import UIkit from 'uikit';

    import LoginService from '../services/LoginService';
    import DataService from '../services/DataService';
    import { User } from '../models/User';
    
    @Component
    export default class Login extends Vue {
        private username = '';
        private password = '';
        private email = '';
        private loading = false;
        private status = true;

        private create(): void {
            LoginService.createUser(this.username, this.email, this.password).then(response => {
                console.log(response);
            });
        }

        private switchStatus(): void {
            this.status = !this.status;
        }
      
        private validate(): void {
            this.loading = true;
            try {
                if(this.status){
                    LoginService.authenticateUser(this.username, this.password).then(response => {
                        if(response.status === 200){
                            this.loading = false;
                            
                            const user: User = {
                                id: response.data.id, 
                                username: response.data.username,
                                token: response.data.token,
                                email: ''
                            };
                            
                            DataService.setData(user);
                            LoginService.getUserToken(user.id).then(response => {
                                if(response.data === LoginService.getUserData().token){
                                    this.$router.push("/dashboard");
                                }
                            });
                        } else {
                            this.loading = false;
                            UIkit.notification({message: "<span uk-icon='icon: trash'></span> Probleem met het inloggen", pos: 'top-left', status: 'danger'});
                        }
                    });
                } else {
                    LoginService.createUser(this.username, this.email, this.password).then((response) => {
                        if(response.status === 200){
                            this.loading = false;
                            this.status = true;
                            UIkit.notification({message: "<span uk-icon='icon: comments'></span>Het maken van een account is gelukt", pos: 'top-left', status: 'success'});
                        } else {
                            this.loading = false;
                            UIkit.notification({message: "<span uk-icon='icon: trash'></span> Probleem met het aanmaken van een account", pos: 'top-left', status: 'danger'});
                        }
                    });
                }
            } finally {
                console.log("Done");
            }
        }
        
    }
    
</script>