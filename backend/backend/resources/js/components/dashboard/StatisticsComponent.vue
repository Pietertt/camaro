<template>
   <div class="uk-card uk-card-default uk-card-body">
    <h3 class="uk-card-title">Statistieken</h3>
        <ul uk-tab>
            <li class="uk-active"><a href="#">Validiteit</a></li>
            <li><a href="#">Per maand</a></li>
        </ul>

        <pie-chart :chart-data="activityData"></pie-chart>
    </div>
</template>

<script lang="ts">

    export default {
       
    }
    
</script>