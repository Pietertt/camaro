<template>
    <div class="uk-position-relative">
        <div class="uk-position-top">
            <menu-component></menu-component>
        </div>
        <div class="uk-section uk-section-muted">
            <div class="uk-container">

                <h3>Welkom, {{username}}</h3>

                <div class="uk-grid-match" uk-grid>

                    <div class="uk-width-1-2">
                        <div class="uk-card uk-card-primary">
                            <div class="uk-card-body">
                                <h3 class="uk-card-title">Statistieken</h3>
                                <table class="uk-table uk-table-hover uk-table-divider uk-table-large">
                                    <thead>
                                        <tr>
                                            <th>Nummer</th>
                                            <th>Datum</th>
                                            <th>Validiteit</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <!-- <tr v-for="d in recentData" :key="d.timestamp" v-on:click="navigate(d[0])"> -->
                                        <tr v-for="d in recentData" :key="d.timestamp" style="cursor: pointer" v-on:click="setId(d[0]); setFootage(d[1])">
                                            <td>{{ d[0] }}</td>
                                            <td>{{ d[1] }}</td>
                                            <td>{{ d[2] }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                    <div class="uk-width-1-2">
                        <div class="uk-card uk-card-secondary">
                            <div class="uk-card-body">
                                <a v-on:click="navigate"><img v-bind:src=imagePath></a>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>




<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import { User } from '../models/User';
    import MenuComponent from '@/components/dashboard/MenuComponent.vue';
    import LoginService from '../services/LoginService';

    @Component({
        components: {
            MenuComponent
        }
    })
    export default class Activities extends Vue {
        private username: string = LoginService.getUserData().username;
        private recentData = [];
        private initId = '';
        private image = '';
        private imagePath = '';
        private route = '';
        private loaded = false;
        private user: User = new User();

        mounted(): void {
            this.loadActivities();
            this.init();
        }

        private setId(id: number){
            this.route = "/activity/" + String(id);
        }

        private navigate(){
            this.$router.push(this.route);
        }

        private init(): void {
            setTimeout(() => {
                this.image = String(this.recentData[0][1]) + '.jpg';
                this.imagePath = 'data/images/' + this.image;
                this.initId = String(this.recentData[0][0]);
                this.route = 'data/activity/data/' + this.initId;
            }, 500);
        }
        
        private setFootage(datum: string){
            this.image = String(datum);
            this.imagePath = 'data/images/' + String(datum) + '.jpg';
            // alert(this.path);
        }

        private loadActivities(): void {
            this.user = LoginService.getUserData();
            axios.get('http://imac-van-pieter.local:5000/activities/all?userid=' + this.user.id).then(response => {
                this.recentData = response.data;
                
            });
        }
    }
    
</script>