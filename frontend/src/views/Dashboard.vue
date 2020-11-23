<template>
    <div class="uk-section uk-section-muted">
        <div class="uk-container">

            <h3>Welkom, Pieter Boersma</h3>

            <div class="uk-grid-match" uk-grid>

                <div class="uk-width-1-4">
                    <menu-component></menu-component>
                </div>

                <div class="uk-width-1-2">
                   <monthly-component></monthly-component>
                </div>

                <div class="uk-width-1-4">
                    <actions-component></actions-component>
                </div>

                <div class="uk-width-1-2">
                    <statistics-component></statistics-component>
                </div>

                <div class="uk-width-1-2">
                    <activities-component></activities-component>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator';
    import axios from 'axios';
    import VueRouter, { Route } from 'vue-router';
    
    import MenuComponent from '@/components/dashboard/MenuComponent.vue';
    import ActionsComponent from '@/components/dashboard/ActionsComponent.vue';
    import MonthlyComponent from '@/components/dashboard/MonthlyComponent.vue';

    @Component({
        components: {
            MenuComponent,
            ActionsComponent,
            MonthlyComponent
        }
    })
    export default class Dashboard extends Vue {
        
    }
    
</script>