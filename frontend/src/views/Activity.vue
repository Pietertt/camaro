<template>
    <div class="uk-position-relative">
        <div class="uk-position-top">
            <menu-component></menu-component>
        </div>
        <div class="uk-section uk-section-default">
            <div class="uk-container">

                <div class="uk-card uk-card-primary uk-card-body uk-margin-bottom">
                    <h3 class="uk-card-title">{{ $route.params.id }}</h3>
                </div>

                <div class="uk-card uk-card-secondary uk-card-body">
                    <video controls class="uk-align-center">
                        <source v-if="loaded" v-bind:src=videoSource>
                    </video>
                </div>

                <div class="uk-card uk-card-default uk-card-body">
                    <p>This security footage was recorded on {{recordedTime}}.</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import LoginService from '../services/LoginService';
    import {User} from '../models/User';
    import MenuComponent from '@/components/dashboard/MenuComponent.vue';

    @Component({
        components: {
            MenuComponent
        }
    })
    export default class Activity extends Vue {
        private recentData = [];
        private videoSource = '';
        private recordedTime;
        private loaded = false;
        private user: User = new User();

        mounted(): void {
            this.loadActivities();
            this.getName(this.$route.params.id)        
        }


        loadActivities(): void {
            this.user = LoginService.getUserData();
            console.log('load activities function');
            axios.get('http://imac-van-pieter.local:5000/activities/all?userid=' + this.user.id).then(response => {
                this.recentData = response.data;
            });
        }

        getName(currentId: string): void {
            setTimeout(() => {
                for (const id of this.recentData){
                    if (id[0] == currentId){
                        this.videoSource = 'data/videos/' + String(id[1]) + '.mp4';
                        this.filterDate(String(id[1]));
                        this.loaded = true;
                        console.log(id);
                    }
                }
            }, 500);
        }

        filterDate(date: string): void {
            this.recordedTime = date.substring(6,8) + "-" + date.substring(4,6) + "-" + date.substring(0,4) + " at " + date.substring(8,10) + ":" + date.substring(10,12) + ":" + date.substring(12,14);
        }
    }
    
</script>