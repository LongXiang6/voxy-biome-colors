package com.lambda.lod.mixin;

import net.minecraft.world.level.ColorResolver;
import net.minecraft.world.level.biome.Biome;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Pseudo;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Redirect;

@Pseudo
@Mixin(targets = "me.cortex.voxy.client.core.model.ModelFactory$2", remap = false)
abstract class VoxySyntheticTintMixin {
    @Redirect(method = "getBlockTint", at = @At(value = "INVOKE",
            target = "Lnet/minecraft/world/level/ColorResolver;getColor(Lnet/minecraft/world/level/biome/Biome;DD)I"))
    private int lambda$resolveTint(ColorResolver resolver, Biome biome, double x, double z) {
        // Voxy's constant-color bake has no biome to pass to a season-aware resolver.
        return biome == null ? -1 : resolver.getColor(biome, x, z);
    }
}
