<template>
    <div class="uk-child-width-expand@s uk-text-center uk-padding-large uk-background-secondary" uk-height-viewport="expand" uk-grid>
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
    import Vue from 'vue'
    import VueRouter from 'vue-router'
    import axios from 'axios'

    import DashboardComponent from './../dashboard/DashboardComponent.vue';

    const routes = [{
        path: '/test',
        name: 'Home',
        component: DashboardComponent
        }
    ];

    const router = new VueRouter({routes
})

    export default {

        

        data(){
            return {
                loading: false,
                username: '',
                password: ''
            }
        },

        methods: {
            validate(){
                this.loading = true;
                axios.post('http://imac-van-pieter.local:4000/valid', {
                    username: this.username,
                    password: this.password
                }).then(response => {
                    this.loading = false;
                    this.$router.push('/dashboard');
                }).catch(error => {
                    this.loading = false;
                });
            }
        }
    }
    
</script>