<template>
    <div class="uk-flex uk-flex-center background">
        <div class="uk-section uk-section-default uk-margin-top uk-margin-bottom uk-padding">
            <div class="uk-container">
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
                                    v-model="usernameLogin">
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
                                    v-model="passwordLogin">
                            </div>
                        </div>
                        <div class="uk-margin">
                            <button class="uk-button uk-form-width-large uk-button-primary">
                                <span v-if="!loadingLogin">Inloggen</span>
                                <span v-if="loadingLogin">
                                    <div uk-spinner></div>
                                </span>
                            </button>
                        </div>
                    </fieldset>
                </form> 
            </div>

            <hr class="uk-divider-icon">

            <div class="uk-container">
                <form v-on:submit.prevent="createAccount">
                    <fieldset class="uk-fieldset">
                        <legend class="uk-legend">Maak een account aan</legend>

                        <div class="uk-margin">
                            <div class="uk-inline">
                                <span class="uk-form-icon" uk-icon="icon: user"></span>
                                <input 
                                    class="uk-input uk-form-width-large" 
                                    type="text" 
                                    placeholder="Gebruikersnaam"
                                    v-model="usernameCreate">
                            </div>
                        </div>
                        <div class="uk-margin">
                            <div class="uk-inline">
                                <span class="uk-form-icon" uk-icon="icon: mail"></span>
                                <input 
                                    class="uk-input uk-form-width-large" 
                                    type="text" 
                                    placeholder="E-mailadres"
                                    v-model="emailCreate">
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
                                <span v-if="!loadingCreate">Maak een account aan</span>
                                <span v-if="loadingCreate">
                                    <div uk-spinner></div>
                                </span>
                            </button>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>      
    </div>
</template>

<style scoped>
    .background {
        background: url(https://images.unsplash.com/photo-1527542146552-9e862c46e596?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1051&q=80);
        background-size: cover;
        height: 100vh;

    }
</style>

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

        private usernameLogin = '';
        private passwordLogin = '';

        private usernameCreate = '';
        private passwordCreate = '';
        private emailCreate = '';


        private loadingLogin = false;
        private loadingCreate = false;
        private status = true;
      
        private validate(): void {
            this.loadingLogin = true;
            try {
                LoginService.authenticateUser(this.usernameLogin, this.passwordLogin).then(response => {
                    if(response.status === 200){
                        this.loadingLogin = false;
                        
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
                        this.loadingLogin = false;
                        UIkit.notification({message: "<span uk-icon='icon: trash'></span> Probleem met het inloggen", pos: 'top-left', status: 'danger'});
                    }
                });
            } finally {
                console.log("Done");
            }
        }

        public createAccount(): void {
            this.loadingCreate = true;
            LoginService.createUser(this.usernameCreate, this.emailCreate, this.passwordCreate).then((response) => {
                if(response.status === 200){
                    this.loadingCreate = false;
                    this.status = true;
                    UIkit.notification({message: "<span uk-icon='icon: comments'></span>Het maken van een account is gelukt", pos: 'top-left', status: 'success'});
                    this.loadingCreate = false;
                } else {
                    this.loadingCreate = false;
                    UIkit.notification({message: "<span uk-icon='icon: trash'></span> Probleem met het aanmaken van een account", pos: 'top-left', status: 'danger'});
                    this.loadingCreate = false;
                }
            });
        }
        
    }
    
</script>