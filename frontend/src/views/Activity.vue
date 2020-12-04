<template>
    <div class="uk-section uk-section-muted">
        <div class="uk-container">
            <div class="uk-card uk-card-secondary">
                <div class="uk-card-body">
                    <h3 class="uk-card-title">Activiteit {{$route.params.id}}</h3>

                </div>
            </div>
            
            <div class="uk-card uk-card-secondary">
            
            </
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import VueRouter, { Route } from 'vue-router';

    export default class Activity extends Vue {

        mounted(): void {
           console.log("Mounted");
        }
        
    }
    
</script>