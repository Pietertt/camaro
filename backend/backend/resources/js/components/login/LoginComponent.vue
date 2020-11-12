<template>
    <div class="uk-child-width-expand@s uk-text-center uk-margin-top" uk-grid>
        <div>

        </div>
        <div>
            <form v-on:submit.prevent="onSubmit">
                <fieldset class="uk-fieldset">
                    <legend class="uk-legend">Inloggen</legend>
                    
                    <div class="uk-margin">
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: user"></span>
                            <input class="uk-input uk-form-width-large" type="text" name="username" placeholder="Gebruikersnaam">
                        </div>
                    </div>

                    <div class="uk-margin">
                        <div class="uk-inline">
                            <span class="uk-form-icon" uk-icon="icon: lock"></span>
                            <input class="uk-input uk-form-width-large" type="password" name="password" placeholder="Wachtwoord">
                        </div>
                    </div>
                    <div class="uk-margin">
                         <button class="uk-button uk-form-width-large uk-button-primary" v-on:click="validate">Inloggen</button>
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

        methods: {
            validate(){
                axios.get('http://imac-van-pieter.local:4000').then(response => {
                    if(response.data == true){
                        this.$router.push('/dashboard')
                    }
                });
            }
        }
    }
    
</script>